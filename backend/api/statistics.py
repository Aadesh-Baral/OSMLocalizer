from flask_restful import Resource
from flask import request

from backend.services.stats_service import StatsService
from backend.services.user_service import UserService
from backend.services.utills import format_and_validate_start_end_date


class HomeStatsAPI(Resource):
    def get(self):
        return StatsService.get_home_page_stats().dict()


class UserLeaderboardAPI(Resource):
    def get(self):
        start_date = request.args.get("startDate", None)
        end_date = request.args.get("endDate", None)
        start_date, end_date = format_and_validate_start_end_date(start_date, end_date)
        return StatsService.get_user_leaderboard(start_date, end_date).dict()


class UserStatSAPI(Resource):
    def get(self, username):
        challenge_id = request.args.get("challengeId", None)
        user = UserService.get_user_by_username(username)
        return StatsService.get_user_stats(user.id, challenge_id).dict()


class ChallengeContributorsStatsAPI(Resource):
    def get(self, challenge_id):
        start_date = request.args.get("startDate", None)
        end_date = request.args.get("endDate", None)
        start_date, end_date = format_and_validate_start_end_date(start_date, end_date)
        return StatsService.get_challenge_contributors_stats(
            challenge_id, start_date, end_date
        ).dict()
