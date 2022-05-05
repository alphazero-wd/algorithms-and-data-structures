const Queue = require("./queue");

/* 
DESIGN A CASHIER CLASS THAT TAKES IN A CUSTOMER OBJECT AND HANDLES FOOD
ORDERING ON A FIRST-COME, FIRST-SERVED BASIS 
*/

/* 
  Here are the requirements:
  1. The cashier requires a customer name and order item for the order.
  2. The customer who was served first is processed first.
  Here are the required implementations:
  • addOrder(customer): Enqueues a customer object to be processed by
  deliverOrder()
  • deliverOrder(): Prints the name and order for the next customer to be
  processed
*/
class Customer {
  constructor(name, order) {
    this.name = name;
    this.order = order;
  }
}

class Cashier {
  constructor() {
    this.customers = new Queue();
  }

  addOrder({ name, order }) {
    this.customers.enqueue(new Customer(name, order));
  }

  deliverOrder() {
    const { name, order } = this.customers.dequeue();
    console.log(`${name}, your ${order} is ready`);
  }
}
