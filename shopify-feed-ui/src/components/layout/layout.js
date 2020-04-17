import React from 'react';
import './layout.scss';

export default class Layout extends React.Component {
    render () {
        return (
            <>
                <header>
                    <b>Shopify Product Feed Genrator</b>
                </header>
                <div className="content-wrapper">
                    {this.props.children}
                </div>
            </>
        );
    }
}