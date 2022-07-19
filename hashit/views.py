from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import hashlib
import json
import hashit.hashes as h


# Create your views here.
def index(request):
    context={}
    return render(request,"hashit/index.html",context)

def get_hash(request):
    hash_code="asdsa"
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        context_to_hash=data["content_to_hash"]
        algorithm = data["algorithm"]

        myHash = h.Hash()
        myHash.hashTest(algorithm,context_to_hash.encode())
        print(algorithm,context_to_hash)
        hash_code = myHash.getHexDigest()

    context = {
        'hash_code':hash_code
    }  
    return JsonResponse(context)