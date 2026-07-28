# SauceDemo Comprehensive Static Test Plan

## Application Overview

Comprehensive test suite covering Authentication, Product Selection, Cart Management, Checkout Form Validations, and Order Overview for SauceDemo.

## Test Scenarios

### 1. Authentication

**Seed:** `seed.spec.ts`

#### 1.1. Successful Login with Valid Standard User Credentials

**File:** `tests/authentication/successful-login.spec.ts`

**Steps:**
  1. Navigate to https://www.saucedemo.com/, enter standard_user and secret_sauce, and click Login.
    - expect: User is redirected to /inventory.html and product inventory list is displayed.

#### 1.2. Login Failure with Locked Out User Account

**File:** `tests/authentication/locked-out-user.spec.ts`

**Steps:**
  1. Navigate to https://www.saucedemo.com/, enter locked_out_user and secret_sauce, and click Login.
    - expect: User remains on login page; error banner displays 'Epic sadface: Sorry, this user has been locked out.'

#### 1.3. Login Failure with Invalid Password

**File:** `tests/authentication/invalid-password.spec.ts`

**Steps:**
  1. Navigate to https://www.saucedemo.com/, enter standard_user and wrong_password, and click Login.
    - expect: Error message 'Epic sadface: Username and password do not match any user in this service' is displayed.

#### 1.4. Login Validation when Required Fields are Blank

**File:** `tests/authentication/blank-fields.spec.ts`

**Steps:**
  1. Navigate to https://www.saucedemo.com/, leave fields blank, and click Login.
    - expect: Error message 'Epic sadface: Username is required' is displayed.

### 2. Products and Cart

**Seed:** `seed.spec.ts`

#### 2.1. Add Single Product to Shopping Cart

**File:** `tests/products/add-single-product.spec.ts`

**Steps:**
  1. Log in and click Add to cart on Sauce Labs Backpack.
    - expect: Cart badge count shows '1' and button text changes to 'Remove'.

#### 2.2. Add Multiple Products and Verify Shopping Cart Badge

**File:** `tests/products/add-multiple-products.spec.ts`

**Steps:**
  1. Log in and click Add to cart on Backpack, Bike Light, and Bolt T-Shirt.
    - expect: Cart badge updates to display '3'.

#### 2.3. Remove Item from Cart Page

**File:** `tests/products/remove-from-cart.spec.ts`

**Steps:**
  1. Navigate to cart page and click Remove next to Sauce Labs Backpack.
    - expect: Item is removed from cart list and badge is cleared.

### 3. Checkout Flow

**Seed:** `seed.spec.ts`

#### 3.1. Successful End-to-End Checkout Flow (Happy Path)

**File:** `tests/checkout/successful-e2e-checkout.spec.ts`

**Steps:**
  1. Add product to cart, proceed to checkout, enter info, review overview, and finish order.
    - expect: Order completed successfully with 'Thank you for your order!' message.

#### 3.2. Checkout Validation - Missing First Name

**File:** `tests/checkout/validation-missing-first-name.spec.ts`

**Steps:**
  1. Leave First Name blank on checkout step one and click Continue.
    - expect: Error banner displays 'Error: First Name is required'.

#### 3.3. Checkout Validation - Missing Postal Code

**File:** `tests/checkout/validation-missing-postal-code.spec.ts`

**Steps:**
  1. Leave Postal Code blank on checkout step one and click Continue.
    - expect: Error banner displays 'Error: Postal Code is required'.

#### 3.4. Cancel Checkout from Overview Page

**File:** `tests/checkout/cancel-checkout-overview.spec.ts`

**Steps:**
  1. Click Cancel on Checkout Overview page.
    - expect: User is redirected to /inventory.html with cart items preserved.

#### 3.5. Verify Item Total, Tax, and Price Calculation on Checkout Overview

**File:** `tests/checkout/price-and-tax-calculation.spec.ts`

**Steps:**
  1. Add Backpack ($29.99) and Bike Light ($9.99) to cart and proceed to Checkout Overview page.
    - expect: Item total shows $39.98, Tax shows $3.20, and Total shows $43.18.
