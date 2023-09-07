import 'bootstrap/dist/css/bootstrap.css'
import Link from 'next/link'
import Lab from './lab'
import Login from './login'
import Navbar from './navbar'

export default function Home() {
  return (
    <div>
      <Navbar></Navbar>
      <Lab></Lab>

     </div>
  )
}