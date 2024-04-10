import { ProductService } from './product.service';
import { Component } from '@angular/core';
import { IProduct } from './Product.model';
import { CartService } from '../cart/cart.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.css']
})
export class CatalogComponent {
  products: any;
  filter: string = '';

  constructor(
    private cartSvc: CartService,
    private productSvc: ProductService ) {}
  
  addToCart(product: IProduct) {
    this.cartSvc.add(product);
  }

  ngOnInit() {
    this.productSvc.getProducts().subscribe((products) => {
      this.products = products;
    });
  }
  
  getFilteredProducts() {
    return this.filter === ''
    ? this.products
    : this.products.filter(
      (product: any) => product.category === this.filter 
    );
  }
}
