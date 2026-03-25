export default function Layout({ children }) {
  return (
    <div className="font-sans">
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
        body { font-family: 'Nunito', sans-serif; }
        * { box-sizing: border-box; }
      `}</style>
      {children}
    </div>
  );
}