import os

from django.shortcuts import redirect
from dropbox import DropboxOAuth2Flow


def front(request):
    authorize_url = __get_dropbox_auth_flow(request).start()
    return redirect(authorize_url)


def __get_dropbox_auth_flow(request):
    redirect_uri = "http://localhost:5000/callback"
    return DropboxOAuth2Flow(
        os.environ["DROPBOX_CLIENT_ID"],
        os.environ["DROPBOX_CLIENT_SECRET"],
        redirect_uri,
        request.session,
        "dropbox-auth-csrf-token"
    )
