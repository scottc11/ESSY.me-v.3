import * as THREE from 'three';
import { Scene } from 'three';
import particlePNG from './assets/cloud-particle.png';
import circlePNG from './assets/circle.png';

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.getElementById("three-container").appendChild( renderer.domElement );

const camera = new THREE.PerspectiveCamera( 55, window.innerWidth / window.innerHeight, 1, 2000 );
camera.position.set( 0, 0, 100 );
camera.lookAt( new THREE.Vector3( 0, 0, 0 ) );

const scene = new Scene();
scene.fog = new THREE.FogExp2( 0x000000, 0.001 );



// PARTCILE VARIABLES
const particleCount = 1800;
const particles = new THREE.Geometry();

// MATERIAL
const material = new THREE.PointsMaterial({ color: 0xFFFFFF, opacity: 0.6, size: 10, transparent: true });

// PARTICLE TEXTURE
const texture = new THREE.TextureLoader().load( './1f46bb094e6b965a3e3b74e9c448a2f4.png', texture => material.map(texture) );

material.color.setHSL( 1.0, 0.3, 0.7 );


for ( let p = 0; p < particleCount; p++ ) {
  // create particles with random positions
  const pX = Math.random() * 500 - 250;
  const pY = Math.random() * 500 - 250;
  const pZ = Math.random() * 500 - 250;

  const particle = new THREE.Vector3(pX, pY, pZ);

  particles.vertices.push(particle);
}


// create the particle systems
const particleSystem = new THREE.Points(particles, material);

scene.add(particleSystem);

renderer.render( scene, camera );




// var svg_html = $('#sphere_asset').html();
// var svg_canvas = document.createElement("canvas");
// canvg(svg_canvas, svg_html);
// var svg_texture = new THREE.Texture(svg_canvas);
