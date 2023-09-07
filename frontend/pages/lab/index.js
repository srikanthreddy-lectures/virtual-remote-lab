import Link from "next/link";
import useSWR from 'swr';

const fetcher = (url) => fetch(url).then((res) => res.json());

export default function Lab() {
  const { data, error, isLoading } = useSWR('/api/staticlabs', fetcher);
 
  if (error) return <div>failed to load</div>
  if (isLoading) return <div>loading...</div>
  let labs = JSON.parse(data)
    return (
      <div style={{marginTop:'2%'}}>
      <div className="container">

        {labs.map(lab => (
        <span key={lab.id}>
          <div className="card shadow p-3 mb-5 bg-body rounded">
            <div className="card-body">
              <h4 className="card-title">{lab.lab} : {lab.title}</h4>
              <p className="card-text">{lab.scenario}</p>
              <Link href={`/lab/lab0${lab.id}`}>
                        <button className="btn btn-primary float-end">Connect Remote Lab</button>
              </Link>
            </div>
          </div>
        </span>
        ))}

      </div>
      </div>
    )
  }