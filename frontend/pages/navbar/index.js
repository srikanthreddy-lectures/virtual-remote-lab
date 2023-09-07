export default function Navbar() {
    return (
        <nav className="navbar navbar-light bg-light ">
        <div className="container">
            <div className="navbar-brand">
                <span className="navbar-logo">
                        <img src="/images/kmit-bar-121x94.png" alt="" style={{height: '3.8rem'}}/>
                </span>
                <span style={{height: '3.8rem', borderLeft: '2px solid black', marginLeft:'5px'}}></span>
                <span style={{fontSize: '30px',marginLeft:'10px'}}>Virtual Remote Cybersecurity Lab</span>
            </div>
        </div>
    </nav>


       
      /*  <nav classNameName="navbar navbar-dark bg-dark">

            <div classNameName="container-fluid">
                <a classNameName="navbar-brand">Virtual Remote Lab</a>
                <div classNameName="d-flex">
                    <Link href={'/register'}>
                        <button classNameName="btn btn-outline-danger">Register</button>
                    </Link>
                    <Link href={'/login'}>
                        <button classNameName="btn btn-outline-primary">Login</button>
                    </Link>
                </div>
            </div>

        </nav> */
    )
}