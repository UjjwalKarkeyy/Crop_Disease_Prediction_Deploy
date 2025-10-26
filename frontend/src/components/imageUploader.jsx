import {useState} from 'react';
import './imageUploaderStyle.css'

const ImageUploader = () =>{
    const[file, setFile] = useState(null);

    const handleFileChange = (e) =>{
        if(e.target.files){
            setFile(e.target.files[0])
        }
    }

    const handleUpload = async () =>{

    }

    return(
        <>
            <div className='input-group'>
                <input id='file' type="file" onChange={handleFileChange}/>
            </div>

            <div className='file-details'>
                {file &&(
                    <section>
                        File details:
                        <ul>
                            <li>
                                Name: {file.name}
                            </li>
                            <li>
                                Type: {file.type}
                            </li>
                            <li>
                                Size: {file.size} bytes
                            </li>
                        </ul>
                    </section>
                )}
            </div>

            {file && (
                <button
                    onClick={handleUpload}
                    className='submit'
                >
                    Upload File</button>
            )}

            <div className='img-preview'>
                {file && (
                    <div className="preview">
                        <h2>Preview of Image</h2>
                        <img src={URL.createObjectURL(file)} alt="preview" height={200}/>
                    </div>
                )}
            </div>
        </>
    )
}

export default ImageUploader;