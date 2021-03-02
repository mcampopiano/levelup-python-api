import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType, Game, Event, Gamer


class EventTests(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # SEED DATABASE WITH ONE GAME TYPE
        # This is needed because the API does not expose a /gametypes
        # endpoint for creating game types
        gametype = GameType()
        gametype.label = "Board game"
        gametype.save()
        game = Game()
        game.game_type_id = 1
        game.title = "Monopoly"
        game.description = "family ending board game"
        game.number_of_players = 4
        game.gamer_id = 1
        game.save()

    def test_create_event(self):
        """
        Ensure we can create a new event.
        """
        

        
        # DEFINE event PROPERTIES
        url = "/events"
        data = {
            "eventTime": "2021-03-02 13:46:38.058841",
            "location": "My house",
            "gameId": 1,
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["event_time"], "2021-03-02 13:46:38.058841")
        self.assertEqual(json_response["location"], "My house")
        self.assertEqual(json_response["game"]["id"], 1)
        self.assertEqual(json_response["scheduler"]["id"], 1)