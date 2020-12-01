with open ("iframe_bypass.html","w") as o:
    print ("<html><body>", file=o)
    print ("<script type=\"module\" src=\"https://unpkg.com/x-frame-bypass\"></script>", file=o)
    
    with open ("url.txt","r") as f:
        for urls in f:
            a = urls.replace("\n","")
            print('<iframe is="x-frame-bypass" src="'+a+'"></iframe>', file=o)
    