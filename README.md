The APIs are :
    * /api/articles/    [GET]

    * /api/login/   [POST]  
        {
            "email" : "",
            "password" : ""
        }
    * /api/article

        [DELETE]    - Deleteing an article
        /api/article/pk=<ID>
        
        [POST]  - Adding new article

        {
            "title" : "",
            "content": "",
            "author" : ""
        }

        [PUT]   - Updating an article

        {
            "id": ,
            "title" : "",
            "content": "",
            "author" : ""
        }

    * /api/articles/search/     [POST]
        {
            "text" : ""
        }

        
        
            