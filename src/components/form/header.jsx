import logo from '../../data/logo.svg'
import '../../assets/style/header.css'
import Button from '../ui/button.jsx'

function Header(title){
	let sub = title;
	let strtitle;
	let imgclass;
	if (sub === ""){
		strtitle = "WolfInfo.ru - " + sub;
			// logo = ImageComponent(0)
	} else {
		strtitle = "WolfInfo.ru";
		imgclass = 'invert'
			// logo = ImageComponent(0)
	};
    return(
        <header>
            <div className='logoplane'>
                <logo>
                    <a href="https://WolfInfo.ru">
                        <image className={imgclass} >
                            <img alt={strtitle} src={logo}/>
                        </image>
                            <logo-text>{strtitle}</logo-text>
                    </a>
                </logo>
            </div>
			<Button/>
        </header>
    );
}

export default Header;