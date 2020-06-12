import React, {Component} from 'react';

class App extends Component {
    state = {
        loading: true,
        conferences: []
    };

    async componentDidMount(){
        const url = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences";
        const response = await fetch(url);
        const data = await response.json();
        this.setState({conferences: data.paid, loading:false});
    }

    render() {
        if (this.state.loading) {
            return <div>loading...</div>;
        }

        if (!this.state.conferences.length) {
            return <div>No conference data available</div>;
        }

        const conferencesJSX = this.state.conferences.map(conference => (
            <div key={conference.conference_id}>
                <div>{conference.confName}</div>
                <div>{conference.venue}</div>
                <div>From : {conference.confStartDate}</div>
                <div>To : {conference.confEndDate}</div>
                <div>{conference.confUrl}</div>
                <div>Register at - {conference.confRegUrl}</div>
                <div>{conference.entryType}</div>
                <img src={conference.imageURL} />
            </div>
        ));

        return <div>{conferencesJSX}</div>
    }
}

export default App;