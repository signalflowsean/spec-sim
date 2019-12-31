import React, { Component } from 'react'; 
import axios from 'axios'

export default class Uploader extends Component { 
  constructor(props) { 
    super(props);

    this.state = { 
      audioFiles : []
    }

    this.API_BASE_URL = "http://localhost:5000"; 

    this.handleChange = this.handleChange.bind(this); 
    this.handleSubmit = this.handleSubmit.bind(this); 
  }

  handleChange(e) {  
    // TODO validation of file extension
    this.setState({ audioFiles: e.target.files })
  }

  handleSubmit(e) { 
    console.log('Submitting form'); 
    e.preventDefault();
    
    let formData = new FormData();
    
    /*
      Iteate over any file sent over appending the files
      to the form data.
    */
    for( var i = 0; i < this.state.audioFiles.length; i++ ){
      let file = this.state.audioFiles[i];
      formData.append('file', file);
    }
    
    // TODO break these api calls into smaller functions
    // UPLOAD FILES TO THE CLOUD
    axios({
      method: 'post',
      url: `${this.API_BASE_URL}/audiolibrary`,
      config: { crossDomain: true }, 
      headers: {'Content-Type': 'multipart/form-data' },
      data: formData 
    })
    // RETRIEVE FEATURES
    .then(result => { 
      let bucketname = result.data; 
      console.info('Successfully posted audio library to backend', bucketname);

      return axios({
        method: 'post',
        url: `${this.API_BASE_URL}/features`,
        config: { crossDomain: true }, 
        headers: {'Content-Type': 'application/json' },
        data: bucketname
      });
    })
    // RETRIEVE SPECTRAL SIMILARITY COORDINATES
    .then(result => { 
      console.info('Sucessfully retrieved features from backend', result.data); 
      return axios({
        method: 'post',
        url: `${this.API_BASE_URL}/coordinates`,
        config: { crossDomain: true }, 
        headers: { 'Content-Type': 'application/json' }
      });
    })
    .then(result => { 
      console.info('Sucessfully retrieved coordinates from backend', result.data)
    })
    .catch(err => { 
      console.error('Error posting audio library to backend: ', err.message); 
    })
  }

  render() { 
    return ( 
      <form encType="multipart/form-data" method="post" onSubmit={this.handleSubmit}>
        <input type="file" name="file" onChange={this.handleChange} webkitdirectory="" directory="" multiple="" />
        <input type="submit" />
      </form>); 
  }
}

