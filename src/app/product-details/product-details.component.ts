import { Component, EventEmitter, Input, Output } from '@angular/core';
import { IProduct } from '../catalog/Product.model';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.css']
})
export class ProductDetailsComponent {
  @Input() product!: IProduct;
  @Output() buy = new EventEmitter();

  cartButtonClicked(product: IProduct){
    this.buy.emit();
  }
}
