import React from "react";
import './Buttons.css';
class Buttons extends React.Component {
    render() {
        return <div className="Buttons"> {this.props.children} </div>
    }
}
export default Buttons;