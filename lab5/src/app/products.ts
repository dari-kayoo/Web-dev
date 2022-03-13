export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  sshow: boolean;
}

export const products = [
  {
    id: 1,
    name: 'Apple iPhone 12 Pro, 128GB',
    price: 799,
    rating: "4.68/5",
    image: 'https://www.technodom.kz/_next/image?url=https%3A%2F%2Fapi.technodom.kz%2Ff3%2Fapi%2Fv1%2Fimages%2F800%2F800%2F228626_1.jpg&w=3840&q=85',
    description: 'A large phone with one of the best screens',
    sshow:false
  },

  {
    id: 2,
    name: 'Apple AirPods (2nd Generation)',
    price: 299,
    rating: "4.33/5",
    image: 'https://reference-audio-analyzer.pro/report/hp/apple/apple-airpods/1.jpg',
    description: 'Effortless setup, in-ear detection, and automatic switching for a magical experience',
    sshow:false
  },
  {
    id: 3,
    name: 'Samsung S21,128gb',
    price: 299,
    rating: "4.88/5",
    image : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXv78JzEym9jaJkxhoOX3a1b4ED_ZH04SgLyKwOvcIAzHAwU3ZOHQbicZby5wJP10xuCE&usqp=CAU',
    description: 'Tested for battery health and guaranteed to come with a battery that exceeds 90% of original capacity.',
    sshow:false
  },
 
  {
    id: 4,
    name: 'Blackberry',
    price: 299,
    rating: "4.35/5",
    image:'https://i.insider.com/5b1e87b61ae6621c008b4a3d?width=1200&format=jpeg',
    description: 'super defenced screen even from 100 km height siuuuuu',
    sshow:false
  },
  {
    id: 5,
    name: 'Macbook M1',
    price: 299,
    rating: "4.75/5",
    image:'https://cdn.vox-cdn.com/thumbor/vGTTyiMMUHIHLs0FjoF0z99m6_E=/0x0:2040x1360/1200x800/filters:focal(895x304:1221x630)/cdn.vox-cdn.com/uploads/chorus_image/image/68592461/vpavic_4291_20201113_0366.0.0.jpg',
    description: 'white, processor M1, the best exepnsive macbook mucha graacios afision',
    sshow:false
  }
  
  
];



/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/