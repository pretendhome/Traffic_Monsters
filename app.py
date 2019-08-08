from flask import Flask

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return """ <html> 
     <body>
    <h2><em>Welcome to the Traffic Monsters Data ETL & Visualization for the City of San Francisco</em></h2>
    <a href="http://tncstoday.sfcta.org/"><img src="https://media3.giphy.com/media/122PZBpK7Z9Aw8/source.gif" alt="GG Bridge"  width=927 height=295 ></a>
    <h3><em>Team Effort<br></em></h3>
    <p>Traffic Monster Members:</p>
        <ul>
        <li>Chi</li>
        <li>Christian</li>
        <li>Mical</li>
        </ul> 
         <h2><em>Project Proposal: San Francisco Ranks as one of the Top Cities in the world for having the worst Traffic Congestion. Can we show that Weather or Rideshare or Construction can have a correlation to the increase of Traffic Congestion in San Francisco?</em></h2>
         <p><em> We have found datasets , extracted data , transformed data , loaded data into databases & used visualization to help us see if those components do play a factor in increased traffic in San Francisco. After analyzing the data we found that the increase of traffic was partially due to the components that have been inspected. Click the Image of the Golden Gate Bridge above to view the Rideshare Dataset that shows the MAX number of rideshare rides that are recorded Monday - Friday in San Francisco . Below are some articles that support the analyzed data.
         </em>
         </p>
         <ul>
         <li>
         <a href="https://www.govtech.com/transportation/Ride-Share-Has-Increased-San-Francisco-Traffic-by-62-Percent.html"><em>Research: Ride Share Has Increased San Francisco Traffic</em></a>
         </em>
         </li>
         <li>
         <a href="https://sf.curbed.com/2017/4/12/15273006/sf-traffic-construction-study"><em>Construction makes terrible San Francisco traffic even worse, says study
</em></a>
         </li>
         </ul>
        <p><del>Before you start writing any code, remember that you only have one week to complete this project. View this project as a typical assignment from work. Imagine a bunch of data came in and you and your team are tasked with migrating it to a production data base.
Take advantage of your Instructor and TA support during office hours and class project work time. They are a valuable resource and can help you stay on track.</del></p>
        <h2><em>Plotted Data & More Visualization</em></h2>
        <ul>
        <li><em>Column Chart & Scatter plot chart Visualizing Top 14 Streets in San Francisco with the Max Rush Hour Traffic</em>
        </li>
        </ul>
        <ul>
        <li>  
        <a href="https://data.sfgov.org/Transportation/Rush-Hour-Routes/4zr7-yz4w"><em></em><img class="panel" src="https://github.com/ChiAmyC0987/ETL-TRAFFIC-MONSTER/blob/master/Images/Rush%20Hour%20Routes%20Max%20Traffic%20Count.png?raw=true"width=540 alt="Rush Hour Max Column"><img class="panel" src="https://github.com/ChiAmyC0987/ETL-TRAFFIC-MONSTER/blob/master/Images/Rush%20Hour%20Traffic%20Routes%20Scatter%20Plot.png?raw=true"width=540 alt="Rush Hour Max Scatter"></a>
        </li>
        </ul>
        <ul>
        <li><em>Bar chart & Pie chart Visualizing Top San Francisco Streets with Maintenance Treatment</em>
        </li>
        <a href="https://data.sfgov.org/City-Infrastructure/Streets-Data-Pavement-Condition-Index-PCI-Scores/5aye-4rtt"><em></em><img class="panel" src="https://github.com/ChiAmyC0987/ETL-TRAFFIC-MONSTER/blob/master/Images/Streets%20Condition%20with%20Max%20Maintenance%20Bar%20Chart.png?raw=true"width=540 alt="SPC"><img class="panel" src="https://github.com/ChiAmyC0987/ETL-TRAFFIC-MONSTER/blob/master/Images/Streets%20Condition%20with%20Max%20Maintenance%20Pie%20Chart.png?raw=true"width=540 alt="SPC pie chart"></a>
       </ul>
       <h2>Data Cleanup & Analysis , Project Report</h2>
        <p>Once you have identified your datasets, perform <strong>ETL</strong> on the data. Make sure to plan and document the following:</p>
       <ul>
        <li><strong>Extract:</strong><br>The sources of data that you will extract from<em>(Datasets were Extracted as CSV files , read & manipulated by using Pandas , Data stored in Postrgres databases managed by PgAdmin4)</em>:</li>
        <br>
        <a href="https://data.sfgov.org/Transportation/Rush-Hour-Routes/4zr7-yz4w"><em>Click: Rush_Hour_Routes.csv</em></a>
        <br></br>
        <a href="https://data.sfgov.org/City-Infrastructure/Streets-Data-Pavement-Condition-Index-PCI-Scores/5aye-
        4rtt"><em>Click: Street_Conditions_2017.csv</em></a>
        <br></br>
        <li><strong>Transform:</strong><br>The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).</li>
        <p><em>Created a filtered dataframe from specific columns</em></p>
        <p><em>Renamed the column headers</em></p>
        <p><em>Cleaned the data by dropping duplicates and setting the index</em></p>
        <p><em>Attempted to combine both csv files with the INNER JOINS clause in PostgresSQL</em></p>
        <li><strong>Load:</strong><br>The type of final production database to load the data into (relational or non-relational).         </li>
        <p><em>Created database , table schema , queries with Pgadmin4 & stored in PostgresSQL / Loaded data into PostgresSQL database from Pandas</em></p>
        <li>The final tables or collections that will be used in the production database.</li>
        <p><em>Loaded DataFrames into PostgresSQL Database as Traffic_db</em></p>
            <p><em>Connected to Network with Mongod</em></p><a href="https://github.com/ChiAmyC0987/ETL-TRAFFIC-MONSTER/blob/master/Images/MongoDBCompassTraffic_db.png?raw=true"><em>Click to View : Created a Database in <strong>MongoDB Compass</strong> as Traffic_db, Imported the 2 CSV files into 2  Collections</em></a>
        <h3>Data Analytic Tools used for Project 1</h3>

<p><em> Jupyter , Python, Pandas , PostgresSQL , PgAdmin4 , MongoD, MongoDB Compass, Flask , Html were used for this project </em></p>


        </body>
        </html>
       

"""


if __name__ == "__main__":
    app.run(debug=True)
