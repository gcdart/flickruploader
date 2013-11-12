import flickr_api;

flickr_api.set_keys(api_key = 'INSERT_API_KEY_HERE' , api_secret = 'INSERT_API_SECRET_HERE' );

auth = flickr_api.auth.AuthHandler();

auth.set_verifier("INSERT_VERIFIER_CODE_HERE");

flickr_api.set_auth_handler(auth);

start = 1;

uploaded = 0;

for line in open('newfilelist'):
  line = line.strip("\n");
  t = line.split("/")[-1].split(".")[0];
  uploaded = uploaded + 1;

  if uploaded >= start:
    print "[" + uploaded + "] Uploading file .. " + line;
    try:
      flickr_api.upload(photo_file = line, title = t);
    except:
      print "[Error] " + uploaded + " lines processed so far. Error while uploading " + line + " in input file.\n";

    
     
