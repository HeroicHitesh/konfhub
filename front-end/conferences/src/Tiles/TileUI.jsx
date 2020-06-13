import React from 'react';
import './tile-style.css';

const Tile = props =>{
    return(
        <div className="card text-center shadow">
            <div className="overflow">
                <img src={props.imgsrc} alt="conference image" className="card-img-top" />
            </div>
            <div className="card-body text-dark">
                <h4 className="card-title">{props.title}</h4>
                <h6>{props.venue}</h6>
                <p className="card-text text-secondary">
                    <b>From :</b> {props.start}<br></br>
                    <b>To :</b> {props.end}<br></br>
                </p>
                <a href={props.site} className="btn btn-outline-primary">Details</a>
                <a href={props.link} className="btn btn-outline-success">Register Now</a>
                <a href="#" className="btn btn-outline-secondary">{props.price}</a>
            </div>
        </div>
    );
}

export default Tile;