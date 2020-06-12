import React, {Component} from 'react'
import Tile from './TileUI';

import img1 from '../assets/192317_web.jpg';
import img2 from '../assets/1396551069000-178795084.jpg';
import img3 from '../assets/kisspng-evil-clown-mask-halloween-costume-circus-clown-5accd1962573f6.0884877315233724381534.jpg'

class Tiles extends Component{
    render(){
        return(
            <div className="container-fluid d-flex justify-content-center">
                <div className="row">
                    <div className="col-md-4"><Tile imgsrc={img1} title="Neuron" /></div>
                    <div className="col-md-4"><Tile imgsrc={img2} title="KeyBoard" /></div>
                    <div className="col-md-4"><Tile imgsrc={img3} title="Joker" /></div>
                </div>
            </div>
        )
    }
}

export default Tiles;