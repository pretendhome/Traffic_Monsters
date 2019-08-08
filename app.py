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
    <h2>Welcome to the Traffic Monsters Data ETL & Visualization for the City of San Francisco</h2>
    <img src="https://media3.giphy.com/media/122PZBpK7Z9Aw8/source.gif" width=827 height=295 />
    <h2>Team Effort<br></h2>
    <p>Traffic Monster Members:</p>
        <ul>
        <li>Chi</li>
        <li>Christian</li>
        <li>Mical</li>
        </ul> 
        <h2>Plotting Data & Visualization</h2>
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
        <li>
        <a href="https://data.sfgov.org/City-Infrastructure/Streets-Data-Pavement-Condition-Index-PCI-Scores/5aye-4rtt"><em></em><img class="panel" src="https://github.com/ChiAmyC0987/ETL-TRAFFIC-MONSTER/blob/master/Images/Streets%20Condition%20with%20Max%20Maintenance%20Bar%20Chart.png?raw=true"width=540 alt="SPC"><img class="panel" src="https://github.com/ChiAmyC0987/ETL-TRAFFIC-MONSTER/blob/master/Images/Streets%20Condition%20with%20Max%20Maintenance%20Pie%20Chart.png?raw=true"width=540 alt="SPC pie chart"></a>
        </li>
        </ul>
       <h2> Project Proposal:</h2>
        <p>Before you start writing any code, remember that you only have one week to complete this project. View this project as a typical assignment from work. Imagine a bunch of data came in and you and your team are tasked with migrating it to a production data base.
Take advantage of your Instructor and TA support during office hours and class project work time. They are a valuable resource and can help you stay on track.</p>
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
            <p><em>Connected to Network with Mongod</em></p><a href="#"><em>Created a Database in <strong>MongoDB Compass</strong> as Traffic_db, Imported the 2 CSV files into 2  Collections</em></a>
        <h3>Data Analytic Tools used for Project 1</h3>

<p><em> Jupyter , Python, Pandas , PostgresSQL , PgAdmin4 , MongoD, MongoDB Compass, Flask , Html were used for this project </em></p>


        </body>
        </html>
       

"""


if __name__ == "__main__":
    app.run(debug=True)
