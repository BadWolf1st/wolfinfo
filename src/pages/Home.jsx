import React from 'react';
import Header from '../components/form/header'
import Team from '../components/form/team'
import Projects from '../components/form/projects'
import '../assets/style/circle.css'
import '../assets/style/maintitle.css'
import '../assets/style/footer.css'
// import {APIClient, config} from '../lib/api'

// const client = new APIClient(config);

function Home(){
	return(
		<div>
			<div className='backg'>
				<div className="circle1"></div>
				<div className="circle2"></div>
			</div>
			<Header/>
			<main>
				<div className='title'>WolfInfo.ru<br/> приветствует вас</div>
				<Team/>
				<Projects/>
			</main>
			<footer>
				<div className='versionfront'>ver DEV5.0</div>
				<div className='footertitle'>by WolfInfo_Team 2021-2024</div>
				<div className='versionapi'>api ver DEV0.1</div>
			</footer>	
		</div>
	);
}

export default Home
