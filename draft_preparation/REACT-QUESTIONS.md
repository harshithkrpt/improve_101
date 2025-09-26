- What is React js

    - React Js By Facebook
    - Open Source Library
    - It helps in Building Single Page Applications
    - Building User Interfaces
    - Building Resuable Components
    - Has Virtual DOM 
        - In Memory Snapshot of original dom

- What is difference between virtual dom and shadow dom, dom in React js 

    - DOM 
        - This is the browser’s tree-like structure representing all the HTML elements.
        - Problem: Slower updates as every update need calculate -> paint 
    - Virtual DOM
        - Lightweight inmemory copy of the DOM
        - React updates its virtual dom in menory as objects
        - At One it will update the real dom
    - Shadow DOM
        - It is a browser feature with web components
        - example <custom-tag> -> uses shadown then the css written in it is encapsulated

- What is controlled and uncontrolled component in React js

    - Controlled Component
        - A controlled component is a form element whose value is controlled by React state.
        - The component does not keep its own internal state for the value—instead, React state is the “single source of truth.”
        ```jsx
            import React, { useState } from "react";

            function ControlledInput() {
            const [name, setName] = useState("");

            return (
                <div>
                <input
                    type="text"
                    value={name}                 // React controls this value
                    onChange={(e) => setName(e.target.value)}
                />
                <p>Typed: {name}</p>
                </div>
            );
            }

        ```
    - UnControlled Component 
        - An uncontrolled component is a form element that manages its own state internally (like how HTML works normally).
        - Instead of React state, you access values using a ref.

        ```jsx
            import React, { useRef } from "react";

            function UncontrolledInput() {
            const nameRef = useRef();

            const handleSubmit = () => {
                alert("Typed: " + nameRef.current.value);
            };

            return (
                <div>
                <input type="text" ref={nameRef} defaultValue="Harshith" />
                <button onClick={handleSubmit}>Submit</button>
                </div>
            );
            }

        ```

| Feature          | Controlled                 | Uncontrolled              |
| ---------------- | -------------------------- | ------------------------- |
| State managed by | React (`useState`)         | DOM (`ref`)               |
| Value prop       | Yes                        | No (uses `defaultValue`)  |
| Access value     | From React state           | From `ref.current.value`  |
| Validation       | Easy, real-time            | Harder, usually on submit |
| Use case         | Dynamic, interactive forms | Simple, one-off forms     |


