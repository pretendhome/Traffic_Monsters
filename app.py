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
    <h2>Welcome to the Traffic Monsters Data Visualization for the City of San Francisco</h2>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwpdcWvUbUPUOvjrt1_VYtw8fl7AhB62rNI2H0HAW4Ms_WtevYPQ" width=767 height=295 />
    <h2>Team Effort<br></h2>
    <p>Traffic Monster Members:</p>
        <ul>
        <li>Chi</li>
        <li>Christian</li>
        <li>Mical</li>
        </ul> 
        <h2>Finding Data & Visualization</h2>
        <ul>
        <li>  
        <a href="https://data.sfgov.org/Transportation/Rush-Hour-Routes/4zr7-yz4w">Click here to see Rush Hour Routes</a>
        </li>
        <li>
        <a href="https://data.sfgov.org/City-Infrastructure/Streets-Data-Pavement-Condition-Index-PCI-Scores/5aye-4rtt">Click Here to see which Streets have the most Maintanence Issues</a>
        </li>
        </ul>
       <h2> Project Proposal:</h2>
        <p>Before you start writing any code, remember that you only have one week to complete this project. View this project as a typical assignment from work. Imagine a bunch of data came in and you and your team are tasked with migrating it to a production data base.
Take advantage of your Instructor and TA support during office hours and class project work time. They are a valuable resource and can help you stay on track.</p>
       <h2>Data Cleanup & Analysis , Project Report</h2>
        <p>Once you have identified your datasets, perform <strong>ETL</strong> on the data. Make sure to plan and document the following:</p>
       <ul>
        <li><strong>Extract:</strong><br>The sources of data that you will extract from<em>(Datasets were Extracted as CSV files , read by using Pandas &   formatted with PgAdmin4)</em>:</li>
        <br>
        <a href="https://data.sfgov.org/Transportation/Rush-Hour-Routes/4zr7-yz4w"><em>Rush_Hour_Routes.csv</em></a>
        <br></br>
        <a href="https://data.sfgov.org/City-Infrastructure/Streets-Data-Pavement-Condition-Index-PCI-Scores/5aye-
        4rtt"><em>Street_Conditions_2017.csv</em></a>
        <br></br>
        <li><strong>Transform:</strong><br>The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).</li>
        <p><em>Created a filtered dataframe from specific columns</em></p>
        <p><em>Renamed the column headers</em></p>
        <p><em>Cleaned the data by dropping duplicates and setting the index</em></p>
        <li><strong>Load:</strong><br>The type of final production database to load the data into (relational or non-relational).         </li>
        <p><em>Created database , table schema , queries via PostgresSQL / Created Database connection via PgAdmin4 </em></p>
        <li>The final tables or collections that will be used in the production database.</li>
        <p><em>Loaded DataFrames into PostgresSQL database</em></p>

<p>You will be required to submit a final technical report with the above information and steps required to reproduce your ETL process.</p>


        </body>
       

"""


if __name__ == "__main__":
    app.run(debug=True)
