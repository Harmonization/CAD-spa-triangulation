import { useState, useEffect } from 'react'
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';

import Cone from './Cone.jsx'

  
  function Scene() {
  
    const [parameters, setParameters] = useState({ h: 2, R: 2, N: 7 })
    const [points, setPoints] = useState([])
    const [normals, setNormals] = useState([])
    const [color, setColor] = useState('#0EFBD4')
    const [border, setBorder] = useState(true)
  
    const keyDown = (parameter, { key, target: { value } }) => {
      if (key === 'Enter' && !isNaN(parseFloat(value))) {
        setParameters(parameters => ({ ...parameters, [parameter]: (parameter !== 'N' ? +value : Math.max(Math.trunc(+value), 2)) }))
      }
    }
  
    useEffect(() => {
      const getPoint = async () => {
        try {
    
          console.log(parameters)
          const response = await fetch(`${import.meta.env.VITE_API_URL}`, { method: 'POST', body: JSON.stringify(parameters) })
          
          if (!response.ok) {
            throw new Error('Network response is no ok!')
          }
          const triangulation = await response.json();
          console.log(triangulation)
          setPoints(triangulation.points)
          setNormals(triangulation.normales)
        } catch (error) {
          console.error('Error fetching data:', error)
        }
      }
      
      getPoint()
    }, [parameters])
  
    const changeColor = ({ target: { value }}) => {
      setColor(value)
    }

    const changeBorder = () => {
      setBorder(!border)
    }
    
    const {R, h} = parameters
    const p1 = R*2+1
    const p2= h*2+1
    const p3 = -R-1

    return (
      <>
      <div className="parameters">
      
        <label htmlFor="input-h">h: </label>
        <input id='input-h' type="number" placeholder='Height' defaultValue={+parameters.h} onKeyDown={e => keyDown('h', e)} />
        <label htmlFor="input-R">R: </label>
        <input id='input-R' type="number" placeholder='Radius' defaultValue={+parameters.R} onKeyDown={e => keyDown('R', e)} />
        <label htmlFor="input-N">N: </label>
        <input id='input-N' type="number" placeholder='Number of segments' defaultValue={+parameters.N} onKeyDown={e => keyDown('N', e)} />
        <label htmlFor="select-colors">Color: </label>
        <input type="color" defaultValue={color} onChange={changeColor}/>
        <label htmlFor="border-check">Border: </label>
        <input type="checkbox" id='border-check' checked={border} onChange={changeBorder}/>
      </div>
      <div className="App">
        <Canvas camera={{position: [-3, -3, 3]}}>
          <ambientLight />
          <pointLight position={[p1, p1, p2]} intensity={40}/>
          <pointLight position={[p3, p3, h]} intensity={4}/>
          <OrbitControls enableZoom={true} />
          <Cone points={points} color={color} normals={normals} border={border}/>
          <axesHelper args={[10]} />

        </Canvas>
      </div>
      </>
    );
  }
  
  export default Scene