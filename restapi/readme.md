<h2> Deployment folder has following structure: </h2>
 <br />
  ├── app.py  # Flask REST API script  <br />
  
  └── models/  <br />
  &nbsp;&nbsp;&nbsp;    └── Contains prediction.py , model.pkl ,class.npy <br />
      
  ├── templates  <br />
   &nbsp;&nbsp;&nbsp;    ├── home.html  <br />
    &nbsp;&nbsp;&nbsp;   └── result.html  <br />
  └── static  <br />
   &nbsp;&nbsp;&nbsp;   └── CSS  <br />
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  └── style.css
         
         
Linear SVC model is used for predictions in rest api.
