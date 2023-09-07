
import useSWR from 'swr';
import React, { useState } from "react";
import ProgressBar from "@ramonak/react-progress-bar";
import Navbar from '../navbar'

//Write a fetcher function to wrap the native fetch function and return the result of a call to url in json format

const fetcher = (url) => fetch(url).then((res) => res.json());

export default function Lab01() {


  const { data, error, isLoading } = useSWR('/api/staticlab01', fetcher);
  const [myurl,setMyUrl]=useState([])
 
  if (error) return <div>failed to load</div>
  if (isLoading) return <div>loading...</div>

  const url_data=async () =>{
    const res = await fetch('http://localhost:5000/mytest')
    setMyUrl(await response.json())
  }

  console.log(myurl)

  //Handle the ready state and display the result contained in the data object mapped to the structure of the json file
  let lab = JSON.parse(data)
  return (
    
     <div>
      <Navbar></Navbar>

        {lab.map(lab => (
          <span key={lab.id}>
              <div className="wrapper flex-container">
                <div className="flex-child title">
                  <h2>{lab.lab} : {lab.title}</h2>
                  <ProgressBar completed={40} />
                </div>
                
                <div className="flex-child remote">
                    <a href={myurl} className="btn btn-primary" target="_blank" >Start Remote Instance</a>
                </div>
              </div>
              <div className="container-fluid">
                <h2>Scenario</h2>
                <p>{lab.scenario}</p>
                <br/>
                <h2>Objective</h2>
                <p>{lab.objective}</p>
                {lab.activities.map(activity => (
                    <div>
                      <span>{activity.chekbox? <input type={'checkbox'}></input> : <span></span>}</span>
                      <span style={{fontSize:'20px',marginLeft:'25px'}}>{activity.title}</span>
                      <p>{activity.desciption}</p>
                      {activity.questions.map(question => (
                        <div style={{marginLeft:'25px'}}>
                           <span >{question.id}</span>
                           <span style={{marginLeft:'15px'}}>{question.question}</span>
                           {question.textbox?<p> <input type={'text'}/><button>Submit</button></p> :<p></p>}
                        </div>
                      ))}
                    </div>
                ))}
              </div>
          </span>
        ))}
        
      
      

      <style jsx>
        {`
          .wrapper {
            background: #e6e6e6;
            padding: 60px 30px;
          }
          .flex-container {
            display: flex;
            justify-content: center;
            align-items: center;
          }
          .flex-child {
            flex: 1;
          }  
          .flex-child:first-child {
            margin-right: 20px;
          } 
          h1 {
            color: black;
          }
          .container {
            background: transparent;
            border: 1px solid #e6e6e6;
            border-radius: 5px;
            // box-shadow: inset 3px 3px 5px rgba(0,0,0,.1), 3px 3px 5px rgba(0,0,0,.1);
            margin-top: 15px;
            margin-bottom: 15px;
            margin-left:10%;
            margin-right:10%;
            padding:10px;
          }
        `}
      </style>
    </div> 
    
  );
    
  }

  