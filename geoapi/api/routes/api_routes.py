from geoapi import api, bcrypt, app, db
from flask import jsonify, request, abort
from flask_restplus import Api, Resource, fields
import jwt
from geoapi.api.helpers.api_helpers import (
    create_account_creds_required,
    token_required,
    refresh_token_required,
    creds_required,
    create_new_user,
    make_new_api_key,
    get_api_keys,
    make_new_refresh_api_key,
    update_password,
    get_geodata
)
from geoapi.api.helpers.description_text import (
    api_description_text,
    ns_geodata_description_text,
    create_account_description_text,
    ns_user_description_text,
    get_new_api_description_text,
    forgot_api_keys_description_text,
    get_new_refresh_api_key_description_text,
    update_password_description_text,
    get_geodata_description_text
)


authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'X-API-KEY'
    }
}

api = Api(
    app,
    authorizations=authorizations,
    title='VIRTUALZERO GEODATA API',
    version='1.0',
    description=api_description_text(),
    validate=True
)

ns_geodata = api.namespace(
    'geodata',
    description=ns_geodata_description_text()
)

ns_user = api.namespace(
    'user',
    description=ns_user_description_text()
)

new_api_user = ns_geodata.model(
    'NewUser', 
    {
        'email': fields.String('email', required=True), 
        'password': fields.String('password', required=True),
        'confirm_password': fields.String('confirm_password', required=True)
    }
)

api_user = ns_geodata.model(
    'User',
    {
        'email': fields.String('email', required=True),
        'password': fields.String('password', required=True)
    }
)

new_password = ns_user.model(
    'UpdatePassword',
    {
        'email': fields.String('email', required=True),
        'password': fields.String('password', required=True),
        'new_password': fields.String('password', required=True)
    }
)


@ns_user.route('/create-account')
class CreateAccount(Resource):
    @ns_user.expect(new_api_user)
    @ns_user.doc(
        description=create_account_description_text()
    )
    @ns_geodata.doc(
        responses={
            200: 'Success', 
            401: 'Not Authorized', 
            500: 'Something went wrong.'
        }
    )
    @create_account_creds_required
    def post(self):
        return create_new_user(), 200


@ns_user.route('/get-new-api-key')
class GetNewAPIKey(Resource):
    @ns_user.doc(
        security='apikey', 
        description=get_new_api_description_text()
    )
    @ns_user.header(
        'X-API-KEY', 
        'Must include the refresh API key in header.'
    )
    @ns_user.doc(
        responses={
            200: 'Success', 
            401: 'Not Authorized', 
            500: 'Something went wrong.'
        }
    )
    @refresh_token_required
    def get(self):
        return make_new_api_key(), 200


@ns_user.route('/forgot-api-keys')
class ForgotAPIKeys(Resource):
    @ns_user.expect(api_user)
    @ns_user.doc(
        description=forgot_api_keys_description_text()
    )
    @ns_user.doc(
        responses={
            200: 'Success', 
            401: 'Not Authorized', 
            500: 'Something went wrong.'
        }
    )
    @creds_required
    def post(self):
        return get_api_keys(), 200


@ns_user.route('/get-new-refresh-api-key')
class GetNewRefreshAPIKey(Resource):
    @ns_user.doc(
        description=get_new_refresh_api_key_description_text()
    )
    @ns_user.expect(api_user)
    @ns_user.doc(
        responses={
            200: 'Success',
            401: 'Not Authorized',
            500: 'Something went wrong.'
        }
    )
    @creds_required
    def post(self):
        return make_new_refresh_api_key(), 200


@ns_user.route('/update-password')
class UpdatePassword(Resource):
    @ns_user.doc(
        description=update_password_description_text()
    )
    @ns_user.expect(new_password)
    @ns_user.doc(
        responses={
            200: 'Success',
            401: 'Not Authorized',
            500: 'Something went wrong.'
        }
    )
    @creds_required
    def post(self):
        return update_password(), 200


@ns_geodata.route('/get-geo-data/<ip_address>')
class Login(Resource):
    @ns_geodata.doc(
        security='apikey', 
        description=get_geodata_description_text()
    )
    @ns_geodata.header(
        'X-API-KEY', 
        'Must include the API key in the header.'
    )
    @ns_geodata.doc(
        responses={
            200: 'Success', 
            401: 'Not Authorized', 
            500: 'Something went wrong.'
        }
    )
    @token_required
    def get(self, ip_address):
        return get_geodata(ip_address), 200
