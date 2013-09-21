simple-circleci
===============

Yay! A python wrapper for the [circleci REST api](https://circleci.com/docs/api). I looked for one so i could build some better build dashboards. none were easy or straight forward. a bunch were in ruby (great! but not for my project). 

Now there is a python one!

---

#Usage: 

Easy

	Python 2.7.2 (default, Oct 11 2012, 20:14:37)
	Type "help", "copyright", "credits" or "license" for more information.
	>>>	
	>>> from simple_circleci import simple_circleci
	>>> api = simple_circleci(token="your_api_key")
	>>> api.me()
	{ … }
	>>> api.projects()
	[ … ]
	>>> len(api.projects())
	10
	>>> print "yay"
	yay
	

Simple

    
    from simple_circleci import simple_circleci
    token = "your_api_key"
    username = "your_username"
    project = "your_project"
    build_number = 1
    api = simple_circleci(token=token)
    print api.me()
    print api.projects()
    print api.recent_builds()
    print api.project(username=username, project=project)
    print api.build(username=username, project=project, build_number=build_number)
    print api.artifacts(username=username, project=project, build_number=build_number)
    print api.build_retry(username=username, project=project, build_number=build_number)
    print api.build_cancel(username=username, project=project, build_number=build_number) 