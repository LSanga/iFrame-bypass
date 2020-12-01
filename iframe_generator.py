with open ("iframe.html","w") as o:
    print ("<html><body>", file=o)
    
    with open ("url.txt","r") as f:
        for urls in f:
            a = urls.replace("\n","")
            print('<iframe src="'+a+'"></iframe>', file=o)
    