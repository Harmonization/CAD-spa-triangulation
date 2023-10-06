import * as THREE from 'three';
import { useEffect } from 'react'

function Cone({ points, color, normals, border }) {

    const geometry = new THREE.BufferGeometry()
    const vertices = new Float32Array(points)
    const normals_array = new Float32Array(normals)
  
    useEffect(() => {
      geometry.setAttribute('position', new THREE.BufferAttribute(vertices, 3))
      geometry.setAttribute('normal', new THREE.BufferAttribute(normals_array, 3, true))

    }, [points, color, border])
  
    return (
      <>
        <mesh  geometry={geometry} >
            <meshStandardMaterial color={color} side={THREE.DoubleSide} transparent={true} opacity={.9} metalness={.3} roughness={.1}/>
        </mesh>
        {border && <mesh geometry={geometry} >
            <meshBasicMaterial color={'black'} wireframe={true} /> 
        </mesh>}
      </>
    )
  }
    
  export default Cone