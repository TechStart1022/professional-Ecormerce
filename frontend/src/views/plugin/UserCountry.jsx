import { useState,useEffect } from "react";

function GetCurrentAddress() {
  const[add,setAdd] = useState('')
  useEffect(()=>{
    navigator.geolocation.getCurrentPosistion(pos => {
      const {latitude,longitude} = pos.coords
      const url =`https://nominatim.openstreetmap.org/reverse?format=json&lat=$lon=${longitude}`

      fetch(url)
      .then(res=>res.json())
      .then(data => setAdd(data,address))
    },[])
  })
  return add
}

export default GetCurrentAddress