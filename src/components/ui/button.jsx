import '../../assets/style/button.css'

function Button(props){
    return(
        <div className='buttonbox logoplane'>
            <label for="toggle" className="hamburger">
                <div classNmae="top-bun"></div>
                <div className="meat"></div>
                <div className="bottom-bun"></div>
            </label>
        </div>
        
    )
}

export default Button;