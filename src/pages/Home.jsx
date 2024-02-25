import React from 'react';
import Header from '../components/form/header'
import '../assets/style/circle.css'

function Home(){
	return(
		<div>
			<div className='backg'>
				<div className="circle1"></div>
				<div className="circle2"></div>
			</div>
			<Header/>	
		</div>
	);
}

export default Home
