import React, {Component} from 'react';

class App extends Component {
    state = {
        loading: true,
        conference: null,
    };

    async componentDidMount(){
        const url = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences";
        const response = await fetch(url);
        const data = await response.json();
        this.setState({conference: data.paid[0], loading:false});
    }

    render() {
        if (this.state.loading) {
            return <div>loading...</div>;
        }

        if (!this.state.conference) {
            return <div>No conference data available</div>;
        }

        return (
            <div>
                <div>{this.state.conference.confName}</div>
                <div>{this.state.conference.venue}</div>
                <div>From : {this.state.conference.confStartDate}</div>
                <div>To : {this.state.conference.confEndDate}</div>
                <div>{this.state.conference.confUrl}</div>
                <div>Register at - {this.state.conference.confRegUrl}</div>
                <div>{this.state.conference.entryType}</div>
                <img src={this.state.conference.imageURL} />
            </div>
        )
    }
}

export default App;