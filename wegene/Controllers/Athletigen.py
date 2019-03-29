# -*- coding: utf-8 -*-

"""
   wegene.Controllers.AthletigenController

   This file was automatically generated by APIMATIC BETA v2.0 on 02/22/2016
"""
import requests

from wegene.APIHelper import APIHelper
from wegene.Configuration import Configuration
from wegene.APIException import APIException
from wegene.Models.Report import Report

class Athletigen(object):


    """A Controller to access Endpoints in the WeGeneAPILib API."""

    def get_athletigen(self,
                    profile_id,
                    report_id):
        """Does a POST request to /athletigen/{profile_id}.

        Athletigen based on genetic information

        Args:
            profile_id (string): Genetic profile id
            report_id (string): Report Id for the specific health risk to
                look

        Returns:
            Report: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/athletigen/{profile_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, {
            "profile_id": profile_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "Authorization": "Bearer " + Configuration.o_auth_access_token,
            "user-agent": "WeGene SDK",
            "accept": "application/json",

        }

        # Prepare parameters
        parameters = {
            "report_id": report_id
        }

        # Prepare and invoke the API call request to fetch the response
        response = requests.post(query_url, headers=headers, data=parameters)

        # Error handling using HTTP status codes
        if response.status_code < 200 or response.status_code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            try:
                return Report(**response.json())
            except TypeError:
                raise APIException("Invalid JSON returned", response.status_code, response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.status_code, response.json())
