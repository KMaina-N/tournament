from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Tournament, Team, Player

# Create your views here.
def index(request):
    """
    Index page of the application
    
    Returns:
        - Rendered template
    """
    tournaments = Tournament.objects.all()
    return render(request, 'index.html', {'tournaments': tournaments})

def add_tournament(request):
    """
    Add tournament to the database
    Handles POST request from the form in add_tournament.html template

    Returns:
        - Redirect to the configure_tournament page
        - Rendered template
    """
    if request.method == 'POST':
        # Get form data from POST request
        tournament_name = request.POST.get('tournament')
        team_count = int(request.POST.get('team_count'))

        # Create a new tournament
        new_tournament = Tournament.objects.create(tournament=tournament_name, team_count=team_count)

        # Populate teams based on the selected number
        teams = []
        for i in range(team_count):
            team = Team.objects.create(tournament=new_tournament, team_name=f'')
            teams.append(team)

        # Pair up teams and set initial opponents
        for i in range(0, team_count, 2):
            teams[i].opponent = teams[i + 1].team_name
            teams[i + 1].opponent = teams[i].team_name
            teams[i].save()
            teams[i + 1].save()

        # Redirect to the team configuration page for the newly created tournament
        return redirect('configure_tournament', tournament_id=new_tournament.id)

    return render(request, 'add_tournament.html')


def configure_tournament(request, tournament_id):
    """ 
    Configure the tournament

    Arguments:
        - tournament_id {int} -- ID of the tournament

    Returns:
        - Rendered template
    """
    # Get the tournament object
    tournament = Tournament.objects.get(pk=tournament_id)
    teams = Team.objects.filter(tournament=tournament)

    return render(request, 'configure_tournament.html', {'tournament': tournament, 'teams': teams})

def add_team(request):
    """
    Add team to the tournament
    request is handled by AJAX

    params:
        - team_name: Name of the team
        - tournament_id: ID of the tournament

    Returns:
        - JsonResponse
    """
    if request.method == 'GET':
        # print the data
        print(request.GET)
        team_name = request.GET.get('team_name')
        team_id = request.GET.get('team_id')
        opponent = request.GET.get('opponent')
        print(team_name, team_id, opponent)
        # update the team name
        team_id = int(team_id)
        team = Team.objects.get(pk=team_id)
        print(team)
        team.team_name = team_name
        team.opponent = opponent
        team.modified = True
        team.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})

def delete_team(request):
    """Delete team from the tournament
    request is handled by AJAX

    params:
        - team_id: ID of the team to be deleted

    Returns:
        - JsonResponse
    """
    if request.method == 'GET':
        team_id = request.GET.get('team_id')
        team_id = int(team_id)
        team = Team.objects.get(pk=team_id)
        team.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})

def view_players(request, team_id):
    """View players of the team
    
    The request redirects to the view_players.html template where you can see the players of the home team and the opponent team.

    Arguments:
        team_id {int} -- ID of the team

    TODO: This function is not yet complete. Implement this function.

    Returns:
        - Rendered template
    """
    team = Team.objects.get(pk=team_id)
    players = Player.objects.filter(team=team)
    return render(request, 'view_players.html', {'players': players, 'team': team})

def add_player(request):
    """Add player to the team
    
    The request is handled by AJAX to make the page more responsive.

    params:
        - player_name: Name of the player
        - team_id: ID of the team

    TODO: Implement this function

    Returns:
        - JsonResponse
    """
    return JsonResponse({'status': 'success'})

def start_tournament(request, tournament_id):
    """
    Start the tournament
    
    This request is not handled by AJAX because we need to redirect to the index page after the tournament is started.

    Arguments:
        - tournament_id {int} -- ID of the tournament

    Returns:
        - Redirect to the index page
    """
    # if request.method == 'GET':
    # tournament_id = request.GET.get('tournament_id')
    print(tournament_id)
    tournament = Tournament.objects.get(pk=tournament_id)
    print(tournament)
    tournament.started = True
    tournament.save()
    # return JsonResponse({'status': 'success'})
    return redirect('index')

def view_results(request, tournament_id):
    """
    View results of the tournament

    Arguments:
        - tournament_id {int} -- ID of the tournament

    TODO: Implement this function

    Returns:
        - Rendered template

    """
    return render(request, 'view_results.html')