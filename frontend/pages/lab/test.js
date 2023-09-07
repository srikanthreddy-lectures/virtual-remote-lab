import { Allotment } from "allotment";
import "allotment/dist/style.css";
import {React,useRef }from "react";
import Login from '../login'
import Split from 'react-split-grid'
import Splitter, { SplitDirection } from '@devbookhq/splitter'



export default function Test() {
 
  /* function handleResizeStarted(gutterIdx: number) {
    console.log('Resize started!', gutterIdx);
  }
  function handleResizeFinished(gutterIdx: number, newSizes: number[]) {
    console.log('Resize finished!', gutterIdx, newSizes);
  } */

  return (
    <div className="wrapper">
     <Splitter >
      <div></div>
      <Login></Login>

     

    </Splitter> 

    <style jsx>
      {`
        .wrapper {
          border-radius: 5px;
          border: 2px solid silver;
          width:100%;
          padding: 2px 2px;
          margin-left:0px;  
          margin-right:20px;
        }
      `}
    </style>
    </div>
    
  );
    
  }

  {/* <div className="wrapper">
  <h1>Hello</h1>

  <style jsx>
    {`
      .wrapper {
        background: #3f51b5;
        padding: 60px 30px;
      }
      h1 {
        color: #ff9800;
      }
    `}
  </style>
</div> */}