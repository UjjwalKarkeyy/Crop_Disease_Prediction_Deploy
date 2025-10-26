import plantImg from '../assets/plant.png'
import "./plantImgStyle.css"

const PlantImgComponent = () => {
  return(
    <div className='plantImg'>
        <img src={plantImg} alt="Image of a plant" height={770} width={380}/>
    </div>
  )
}

export default PlantImgComponent;