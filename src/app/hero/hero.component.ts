import { Component } from '@angular/core';

@Component({
  selector: 'app-hero',
  templateUrl: './hero.component.html',
  styleUrls: ['./hero.component.css']
})
export class HeroComponent {
  headerLabel: string = "Simple Shoping Website";
  navbar: any[] = [
    {label: "Home", link: "/home"},
    {label: "Products", link: "/catalog"},
    {label: "Cart", link: "/cart"},
  ];
}
