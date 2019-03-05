## PSA internal storage

PSA internal storage APIs enable saving data to and retrieving data from a PSA internal flash.

The implementation of PSA internal storage varies depending on the target type:

* On a single core ARMv7-M target, PSA internal storage APIs are implemented by calling the default internal TDBStore instance.
* On PSA targets that implement Secure Partition Manager (SPM), PSA internal storage is implemented as a secure service. The service uses an access control list to ensure that it only accesses entries created from the Non-Secure Processing Environment (NSPE).

### PSA internal storage class reference

[![View code](https://www.mbed.com/embed/?type=library)](xxx)

### Example

### Related content

* [Storage overview (Mbed OS)](..apis/storage.html).

* [PSA secure storage](https://pages.arm.com/PSA-APIs).