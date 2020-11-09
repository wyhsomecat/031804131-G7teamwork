def test(req):
    if req.method=="GET":
        imglist=models.Img.objects.all().values_list("img_path")
        return render(req,"test.html",{"imglist":imglist})
    elif req.method=="POST":
        user=req.POST.get("user")
        file=req.FILES.get("testfile")
        path=os.path.join("static","imgs",file.name)
        with open(path,"wb") as f:
            for chunk in file.chunks():
                f.write(chunk)
        print(user,file.name,file.size)
        models.Img.objects.create(img_path=path)
        return redirect("/test/")
