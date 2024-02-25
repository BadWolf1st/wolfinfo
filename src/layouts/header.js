import React from 'react'
import '../assets/style/header.css'
// import ImageComponent from '../../src/lib/images.js' 
import logo from '../data/logo.svg'

class Header extends React.Component(){
	// sub = this.props.title;

	// if (sub = ""){
	// 	let title = "WolfInfo.ru - " + sub;
	// 		// logo = ImageComponent(0)
	// } else {
	// 	let title = "WolfInfo.ru";
	// 		// logo = ImageComponent(0)
	// };
	// const logo = 'src/data/logo.svg';
	render(){
		return(
			<header class="position-absolute top-0 start-0">
				<a href="https://WolfInfo.ru" target="_self">
					<image>
						<img alt="WolfInfo.ru" class="d-inline-block align-text-top invert" src={logo}/>
					</image>
				</a>
			</header>
		);
	};
}

export default Header
