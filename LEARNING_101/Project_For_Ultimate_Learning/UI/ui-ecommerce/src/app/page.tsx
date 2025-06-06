"use server"
import React from 'react';


export default async function Home(props) {
  console.log({props})
  return (
    <div className="p-6">
    
      <p>This is your protected Home page.</p>
    </div>
  );
}
