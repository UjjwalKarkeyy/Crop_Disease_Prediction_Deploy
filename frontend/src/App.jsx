import PlantImgComponent from "./components/plantImg";
import './App.css'
import ImageUploader from "./components/imageUploader";

function App(){
  return(
    <>
    <div className="main-content">
      <h1 id="title">Crop Disease Prediction</h1>
      <h2 id="instruction">Upload Your Image Below</h2>
      <ImageUploader/>
    </div>
      <PlantImgComponent />
    </>
  )
}

export default App;