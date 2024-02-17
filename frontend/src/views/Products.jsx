import {useState, useEffect} from 'react'
import {useNavigate,Link} from 'react-router-dom'
import axios from 'axios'



const  Products = () => {
    const [products, setProducts] = useState([])
    const [category,setCategory] = useState([])

    useEffect(()=>{
        const fetchData = async() => {
            try{
                await axios.get('http://localhost:8000/api/v1/products/').then((res)=>{
                    setProducts(res.data)
                })
            }catch(error){
                alert(error.response.data)
            }
        }
        fetchData()
    },[])
    useEffect(()=>{
        const fetchData = async() => {
            try{
                await axios.get('http://localhost:8000/api/v1/category/').then((res)=>(
                    setCategory(res.data)
                ))
            }catch(error){
                alert(error.response.data)
            }
        }
        fetchData()
    },[])
    console.log(category)

    
    return (
        <div>
        <main className="mt-5">
            <div className="container">
                <section className="text-center">
                    <div className="row">
                        {products?.map((product,index)=>(
                            <div className="col-lg-4 col-md-12 mb-4">
                                <div className="card">
                                    <div
                                        className="bg-image hover-zoom ripple"
                                        data-mdb-ripple-color="light"
                                    >
                                        <img
                                            src={product.image}
                                            className="w-100"
                                        />
                                        <a href="#!">
                                            <div className="mask">
                                                <div className="d-flex justify-content-start align-items-end h-100">
                                                    <h5><span className="badge badge-primary ms-2">New</span></h5>
                                                </div>
                                            </div>
                                            <div className="hover-overlay">
                                                <div
                                                    className="mask"
                                                    style={{ backgroundColor: "rgba(251, 251, 251, 0.15)" }}
                                                />
                                            </div>
                                        </a>
                    </div>
                    <div className="card-body">
                      <a href="" className="text-reset">
                        <h5 className="card-title mb-3">{product.title}</h5>
                      </a>
                      <a href="" className="text-reset">
                        <p>{product.category.title}</p>
                      </a>
                      <div className="d-flex justify-content-center">
                        <h6 className="mb-3">${product.price}</h6>
                        <h6 className="mb-3 text-muted ms-2"><strike>${product.old_price}</strike></h6>
                      </div>

                      <div className="btn-group">
                        <button
                          className="btn btn-primary dropdown-toggle"
                          type="button"
                          id="dropdownMenuClickable"
                          data-bs-toggle="dropdown"
                          data-bs-auto-close="false"
                          aria-expanded="false"
                        >
                          Variation
                        </button>
                        <ul
                          className="dropdown-menu"
                          aria-labelledby="dropdownMenuClickable"
                        >
                          <div className="d-flex flex-column">
                            <li className="p-1">
                              <b>Size</b>: XL
                            </li>
                            <div className="p-1 mt-0 pt-0 d-flex flex-wrap">
                              <li>
                                <button className="btn btn-secondary btn-sm me-2 mb-1">
                                  XXL
                                </button>
                              </li>
                              <li>
                                <button className="btn btn-secondary btn-sm me-2 mb-1">
                                  XXL
                                </button>
                              </li>
                              <li>
                                <button className="btn btn-secondary btn-sm me-2 mb-1">
                                  XXL
                                </button>
                              </li>
                            </div>
                          </div>
                          <div className="d-flex flex-column mt-3">
                            <li className="p-1">
                              <b>COlor</b>: Red
                            </li>
                            <div className="p-1 mt-0 pt-0 d-flex flex-wrap">
                              <li>
                                <button
                                  className="btn btn-sm me-2 mb-1 p-3"
                                  style={{ backgroundColor: "red" }}
                                />
                              </li>
                              <li>
                                <button
                                  className="btn btn-sm me-2 mb-1 p-3"
                                  style={{ backgroundColor: "green" }}
                                />
                              </li>
                              <li>
                                <button
                                  className="btn btn-sm me-2 mb-1 p-3"
                                  style={{ backgroundColor: "yellow" }}
                                />
                              </li>
                            </div>
                          </div>
                          <div className="d-flex mt-3 p-1">
                            <button
                              type="button"
                              className="btn btn-primary me-1 mb-1"
                            >
                              <i className="fas fa-shopping-cart" />
                            </button>
                            <button
                              type="button"
                              className="btn btn-danger px-3 me-1 mb-1 ms-2"
                            >
                              <i className="fas fa-heart" />
                            </button>
                          </div>
                        </ul>
                        <button
                          type="button"
                          className="btn btn-danger px-3 me-1 ms-2"
                        >
                          <i className="fas fa-heart" />
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
                ))}
                    <div className="row">
                        {category?.map((c,index)=>(
                        <div className="col-lg-2">
                            <Link to={`/detail/${p.slug}`}><img src={c.image} style={{width:"100px",height:"100px",borderRadius:"50%",objectFit:"cover"}}/></Link>
                            <h6>{c.title}</h6>
                        </div>
                        ))}
                    </div>
                </div>
            </section>
          </div>
        </main>
      </div>
)
}
export default Products