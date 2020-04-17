import React from 'react';
import './add-feed.scss';
export default class AddFeed extends React.Component {
    state = {
        productName: '',
        tags: '',
        salePrice: '',
        mrp: '',
        itemCost: '',
        size: ["S","M","L","XL","XXL","3XL"],
        black: '',
        white: '',
        red: '',
        royalBlue: '',
        charcoalGrey: '',
        melangeGrey: '',
        navyBlue: '',
        oliveGreen: '',
        goldenYellow: '',
        skyBlue: '',
        lightPink: '',
        productList: []
    };
    changeFields(label, event) {
        const obj = {};
        obj[label] = event.target.value;
        this.setState(obj);
    }
    render () {
        const { productList, productName, tags, salePrice, mrp, itemCost, size, black, white, red, charcoalGrey, goldenYellow, lightPink, melangeGrey, navyBlue, oliveGreen, royalBlue, skyBlue } = this.state;
        return (
            <div className="add-feed-container">
                <div className="column add-prduct-form">
                    <input value={productName} type="text" className="hk-textbox" placeholder="Product Name" onChange={this.changeFields.bind(this, 'productName')}/>
                    <input value={tags} type="text" className="hk-textbox" placeholder="Tags eg: Tag1, Tag2 ..." onChange={this.changeFields.bind(this, 'tags')}/>
                    <input value={salePrice} type="text" className="hk-textbox" placeholder="Sale Price" onChange={this.changeFields.bind(this, 'salePrice')}/>
                    <input value={mrp} type="text" className="hk-textbox" placeholder="MRP" onChange={this.changeFields.bind(this, 'mrp')}/>
                    <input value={itemCost} type="text" className="hk-textbox" placeholder="Item Cost" onChange={this.changeFields.bind(this, 'itemCost')}/>
                    {/* <input value={size} type="text" className="hk-textbox" placeholder="Size eg: Size1, Size2, Size3..." onChange={this.changeFields.bind(this, 'size')}/> */}
                    <div className="color-wrapper">
                        <span className="main-title"><b>Colors</b></span>
                        <div className="group-input">
                            <span>BLACK</span>
                            <input value={black} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'black')}/>    
                        </div>
                        <div className="group-input">
                            <span>WHITE</span>
                            <input value={white} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'white')}/>        
                        </div>
                        <div className="group-input">
                            <span>RED</span>
                            <input value={red} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'red')}/>        
                        </div>
                        <div className="group-input">
                            <span>ROYAL BLUE</span>
                            <input value={royalBlue} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'royalBlue')}/>        
                        </div>
                        <div className="group-input">
                            <span>CHARCOAL GREY</span>
                            <input value={charcoalGrey} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'charcoalGrey')}/>        
                        </div>
                        <div className="group-input">
                            <span>MELANGE GREY</span>
                            <input value={melangeGrey} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'melangeGrey')}/>        
                        </div>
                        <div className="group-input">
                            <span>NAVY BLUE</span>
                            <input value={navyBlue} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'navyBlue')}/>        
                        </div>
                        <div className="group-input">
                            <span>OLIVE GREEN</span>
                            <input value={oliveGreen} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'oliveGreen')}/>        
                        </div>
                        <div className="group-input">
                            <span>GOLDEN YELLOW</span>
                            <input value={goldenYellow} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'goldenYellow')}/>        
                        </div>
                        <div className="group-input">
                            <span>SKY BLUE</span>
                            <input value={skyBlue} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'skyBlue')}/>        
                        </div>
                        <div className="group-input">
                            <span>LIGHT PINK</span>
                            <input value={lightPink} type="text" className="hk-textbox" onChange={this.changeFields.bind(this, 'lightPink')}/>        
                        </div>
                        <div className="group-input right">
                            <button className="hk-button save" onClick={this.onSaveProduct.bind(this)}>SAVE</button>
                        </div>
                        
                    </div>
                </div>
                <div className="column product-list">
                    <span className="title"><b>Product List</b></span>
                    {this.state.productList.map((product, index) => {
                        return (
                            <div className="list-item" key={index}>
                                <img alt="product" src='data:image/jpeg;base64,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' />
                                <span>{product.product_name}</span>
                                <label onClick={this.onRemoveProduct.bind(this, index)}>X</label>
                            </div>
                        );
                    })}
                    {!this.state.productList || this.state.productList.length <= 0 ?
                        <span className="empty-msg">No Products added</span>:''
                    }
                    {this.state.productList && this.state.productList.length > 0 ?
                        <button className="hk-button save" onClick={this.onDownloadFeed.bind(this)}>DOWNLOAD FEED</button>:''
                    }       
                    
                </div>
            </div>
        );
    }
    onRemoveProduct(index) {
        const productList = this.state.productList;
        productList.splice(index, 1);
        this.setState({productList});
    }
    onDownloadFeed() {

    }
    onSaveProduct() {
        const { productList, productName, tags, salePrice, mrp, itemCost, size, black, white, red, charcoalGrey, goldenYellow, lightPink, melangeGrey, navyBlue, oliveGreen, royalBlue, skyBlue } = this.state;
        productList.push({
            "product_name": productName,
            "colorsImageMap": {
                "BLACK": black,
                "WHITE": white,
                "RED": red,
                "ROYAL BLUE": royalBlue,
                "CHARCOAL GREY": charcoalGrey,
                "MELANGE GREY": melangeGrey,
                "NAVY BLUE": navyBlue,
                "OLIVE GREEN": oliveGreen,
                "GOLDEN YELLOW": goldenYellow,
                "SKY BLUE": skyBlue,
                "LIGHT PINK": lightPink
            },
            "tags": tags,
            "sale_price": salePrice,
            "mrp": mrp,
            "item_cost": itemCost,
            "size": size
        });
        this.setState({
            productName: '',
            tags: '',
            salePrice: '',
            mrp: '',
            itemCost: '',
            size: ["S","M","L","XL","XXL","3XL"],
            black: '',
            white: '',
            red: '',
            royalBlue: '',
            charcoalGrey: '',
            melangeGrey: '',
            navyBlue: '',
            oliveGreen: '',
            goldenYellow: '',
            skyBlue: '',
            lightPink: '',
            productList
        });
    }
}